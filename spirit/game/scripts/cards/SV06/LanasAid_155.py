from spirit.game.data_utils import SupporterCardDef, has_rule_box
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.session.effects import is_pokemon_card


async def lanas_aid(ctx):
    pokemon_candidates = [
        c for c in ctx.discard_pile()
        if is_pokemon_card(c) and not has_rule_box(c.archetype_id)
    ]
    energy_candidates = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    candidates = pokemon_candidates + energy_candidates

    if not candidates:
        return

    picks = await ctx.choose_cards(
        candidates,
        3,
        minimum=0,
        prompt=(
            "Choose up to 3 cards to put into your hand "
            "(Pokémon without a Rule Box and Basic Energy)."
        ),
    )
    if picks:
        await ctx.put_in_hand(picks, reveal=False)


card = SupporterCardDef(
    guid="7bd8c33d-34b4-4713-b2b9-b9da858fd273",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.LanasAid.Name",
    display_name="Lana's Aid",
    searchable_by=["Lana's Aid", "Supporter", "LanasAid"],
    subtypes=["Supporter"],
    collector_number=155,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=lanas_aid,
)

