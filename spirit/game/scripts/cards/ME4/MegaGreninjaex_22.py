from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type, in_active_spot
from spirit.game.card_effects.support_common import requires_hand
from spirit.game.card_effects.trainers import is_basic_energy_card, is_water_energy_card


def _is_basic_water_energy(card):
    return is_basic_energy_card(card) and is_water_energy_card(card)


def _mortal_shuriken_condition(board, player_id, pokemon):
    if not in_active_spot(board, player_id, pokemon):
        return False
    return requires_hand(_is_basic_water_energy)(board, player_id, pokemon)


async def mortal_shuriken(ctx):
    """Discard a Basic Water Energy from hand, then place 6 damage counters
    on 1 of your opponent's Pokemon."""
    discarded = await ctx.discard_from_hand(
        1, predicate=_is_basic_water_energy,
        prompt="Discard a Basic Water Energy card to use Mortal Shuriken",
    )
    if not discarded:
        return
    candidates = ctx.opponent_pokemon_in_play()
    if not candidates:
        return
    target = await ctx.choose_pokemon(
        candidates, "Choose 1 of your opponent's Pokémon",
    )
    if target is None:
        return
    await ctx.place_damage_counters(6, [target])


def _is_water_energy(card):
    return energy_provides_type(card, PokemonTypes.WATER.value)


async def ninja_spinner(ctx):
    """120, +80 more if you put an attached Water Energy into your hand."""
    energies = [e for e in ctx.attached_energies(ctx.attacker) if _is_water_energy(e)]
    bonus = 0
    if energies and await ctx.ask_yes_no(
        "Put a Water Energy attached to this Pokémon into your hand? "
        "If you do, this attack does 80 more damage."
    ):
        picks = await ctx.choose_cards(
            energies, 1, prompt="Choose a Water Energy card to put into your hand",
        )
        if picks:
            await ctx.put_in_hand(picks, reveal=False)
            bonus = 80
    await ctx.deal_damage(120 + bonus)


card = PokemonCardDef(
    guid="948404e8-9a92-589d-8056-03202ec63e84",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaGreninjaex.Name",
    display_name="Mega Greninja ex",
    searchable_by=["Mega Greninja ex","Stage 2","ex","SV_Mega","MegaGreninjaex"],
    subtypes=["Stage 2","ex","SV_Mega"],
    collector_number=22,
    set_code="ME4",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=350,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frogadier.Name",
    family_id=656,
    abilities=[
        Ability(
            title="Mortal Shuriken",
            game_text="Once during your turn, if this Pokémon is in the Active Spot, you may discard a Basic Water Energy card from your hand in order to use this Ability. Place 6 damage counters on 1 of your opponent's Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_mortal_shuriken_condition,
            effect=mortal_shuriken,
        ),
        Attack(
            title="Ninja Spinner",
            game_text="You may put a Water Energy attached to this Pokémon into your hand and have this attack do 80 more damage.",
            cost={PokemonTypes.WATER: 2},
            damage=120,
            damage_operator="+",
            effect=ninja_spinner,
        ),
    ],
)
