from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.card_effects.trainers import is_basic_energy_card


async def _powerglass(ctx):
    """At the end of your turn, if Active, you may attach a Basic Energy
    from your discard pile to this Pokémon."""
    pokemon = ctx.source
    if ctx.session.turn_state.active_player_id != ctx.player_id:
        return
    if not is_in_active_spot(pokemon):
        return
    energy = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    if not energy:
        return
    if not await ctx.ask_yes_no(
        "Attach a Basic Energy from your discard pile to this Pokémon?"
    ):
        return
    picks = await ctx.choose_cards(
        energy, 1, minimum=1,
        prompt="Choose a Basic Energy card to attach.",
    )
    if picks:
        await ctx.attach_energy(picks[0], pokemon)


card = PokemonToolCardDef(
    guid="9b13e2b2-c8fb-5e6a-90f6-0416af522c16",
    key="SV065",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Powerglass.Name",
    display_name="Powerglass",
    searchable_by=["Powerglass","Pokémon Tool","Tool","Powerglass"],
    subtypes=["Pokémon Tool","Tool"],
    collector_number=63,
    set_code="SV065",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Powerglass",
            game_text="At the end of your turn (after your attack), if the Pokémon this card is attached to is in the Active Spot, you may attach a Basic Energy card from your discard pile to it.",
            trigger=Triggers.BETWEEN_TURNS,
            effect=_powerglass,
        ),
    ],
)
