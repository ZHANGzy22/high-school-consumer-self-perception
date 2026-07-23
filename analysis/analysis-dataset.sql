-- One row per participant for analysis.
-- Read-only query. Completion quality is checked with valid_complete.
with ranked_decisions as (
  select
    e.*,
    row_number() over (
      partition by e.session_id, e.stage
      order by e.event_order desc, e.id desc
    ) as stage_rank
  from public.simulation_events e
  where e.event_type in ('decision', 'shopping_decision', 'timeout')
    and e.stage in ('feed', 'popup', 'detail', 'checkout', 'review')
),
decisions as (
  select
    session_id,
    max(action) filter (where stage = 'feed' and stage_rank = 1) as feed_action,
    max(action) filter (where stage = 'popup' and stage_rank = 1) as popup_action,
    max(action) filter (where stage = 'detail' and stage_rank = 1) as detail_action,
    max(action) filter (where stage = 'checkout' and stage_rank = 1) as checkout_action,
    max(action) filter (where stage = 'review' and stage_rank = 1) as review_action,
    max(decision_time_ms) filter (where stage = 'feed' and stage_rank = 1) as feed_time_ms,
    max(decision_time_ms) filter (where stage = 'popup' and stage_rank = 1) as popup_time_ms,
    max(decision_time_ms) filter (where stage = 'detail' and stage_rank = 1) as detail_time_ms,
    max(decision_time_ms) filter (where stage = 'checkout' and stage_rank = 1) as checkout_time_ms,
    max(decision_time_ms) filter (where stage = 'review' and stage_rank = 1) as review_time_ms,
    bool_or(interest_product) filter (where stage_rank = 1) as interest_product,
    max(price) filter (where stage_rank = 1) as selected_price,
    max(budget_pressure) filter (where stage_rank = 1) as budget_pressure_pct,
    count(*) filter (where stage_rank = 1) as completed_stage_count,
    count(*) filter (where stage_rank = 1 and action = 'timeout') as timeout_count
  from ranked_decisions
  group by session_id
),
base as (
  select
    s.id as session_id,
    s.app_version,
    s.started_at,
    rf.completed_at,
    nullif(s.profile ->> 'grade', '') as grade,
    (s.profile ->> 'budget')::numeric as budget_yuan,
    s.profile -> 'categories' as recent_categories,
    (s.self_assessment -> 'consumer_self_perception' ->> 'budget_impact')::int as self_budget,
    (s.self_assessment -> 'consumer_self_perception' ->> 'review_split')::int as self_info,
    (s.self_assessment -> 'consumer_self_perception' ->> 'extra_service')::int as self_detail,
    (s.self_assessment -> 'consumer_self_perception' ->> 'price_drop')::int as self_time,
    (s.self_assessment -> 'awareness_pre_items' ->> 'predict_choice')::int as pre_predict,
    (s.self_assessment -> 'awareness_pre_items' ->> 'plan_action_match')::int as pre_match,
    (s.self_assessment -> 'awareness_pre_items' ->> 'know_influences')::int as pre_influences,
    (rf.profile_label_details -> 'awareness_post_items' ->> 'predict_choice')::int as post_predict,
    (rf.profile_label_details -> 'awareness_post_items' ->> 'plan_action_match')::int as post_match,
    (rf.profile_label_details -> 'awareness_post_items' ->> 'know_influences')::int as post_influences,
    rf.profile_label,
    rf.label_fit,
    rf.reflection,
    rf.influence_notes,
    d.*
  from public.sessions s
  left join decisions d on d.session_id = s.id
  left join public.result_feedback rf on rf.session_id = s.id
),
scored as (
  select
    *,
    (completed_at is not null and completed_stage_count = 5) as valid_complete,
    (self_budget >= 4 and review_action = 'review_submit' and budget_pressure_pct >= 20)::int as budget_gap,
    (self_info >= 4 and coalesce(detail_action, '') not in ('detail_review', 'detail_rule')
      and coalesce(review_action, '') <> 'review_more')::int as info_gap,
    (self_detail >= 4 and checkout_action = 'checkout_keep')::int as default_gap,
    (self_time >= 4 and popup_action = 'popup_view' and popup_time_ms <= 10000
      and (detail_action in ('detail_buy', 'detail_cart') or review_action = 'review_submit'))::int as time_gap,
    round(((pre_predict - post_predict) + (pre_match - post_match)
      + (post_influences - pre_influences))::numeric / 3, 2) as recalibration_score
  from base
)
select
  *,
  budget_gap + info_gap + default_gap + time_gap as mismatch_count
from scored
order by started_at;
