from spirit.game.data_utils import PokemonToolCardDef, Ability, Triggers
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot


async def _punk_helmet_trigger(ctx):
    pokemon = ctx.source
    if not is_in_active_spot(pokemon):
        return
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    if PokemonTypes.DARKNESS.value not in types:
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    await ctx.deal_damage(40, target=attacker, apply_modifiers=False, as_counters=True)


card = PokemonToolCardDef(
    guid="0c8c26f4-0c27-53a2-bc2a-e73d58b205f3",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.PunkHelmet.Name",
    display_name="Punk Helmet",
    searchable_by=["Punk Helmet","Pokémon Tool","Tool","PunkHelmet"],
    subtypes=["Pokémon Tool","Tool"],
    collector_number=92,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    granted_abilities=[
        Ability(
            title="Punk Helmet",
            game_text="If the Darkness Pokémon this card is attached to is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), place 4 damage counters on the Attacking Pokémon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=_punk_helmet_trigger,
        ),
    ],
)
