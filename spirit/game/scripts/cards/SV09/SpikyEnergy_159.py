from spirit.game.data_utils import EnergyCardDef, Ability, Triggers
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import is_in_active_spot


async def _spiky_energy_trigger(ctx):
    pokemon = ctx.source
    if not is_in_active_spot(pokemon):
        return
    attacker = ctx.damaged_by
    if attacker is None or attacker.owning_player_id == pokemon.owning_player_id:
        return
    await ctx.deal_damage(20, target=attacker, apply_modifiers=False, as_counters=True)


card = EnergyCardDef(
    guid="a1609c13-6330-50b6-9d7a-1cf85f78fe70",
    key="SV09",
    name="Spiky Energy",
    display_name="Spiky Energy",
    searchable_by=["Spiky Energy", "Special", "SpikyEnergy"],
    subtypes=["Special"],
    collector_number=159,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    energy_type=PokemonTypes.COLORLESS,
    is_special=True,
    granted_abilities=[
        Ability(
            title="Spiky Energy",
            game_text="If the Pokémon this card is attached to is in the Active Spot and is damaged by an attack from your opponent's Pokémon (even if this Pokémon is Knocked Out), put 2 damage counters on the Attacking Pokémon.",
            trigger=Triggers.ON_DAMAGED_BY_ATTACK,
            effect=_spiky_energy_trigger,
        ),
    ],
)
