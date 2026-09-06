import random

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.support_common import distribute_energy


def _is_basic_metal_energy(card) -> bool:
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_basic_energy_card(card) and PokemonTypes.METAL.value in types


async def metal_maker(ctx):
    """Look at the top 4; attach any Basic [M] Energy found there to your
    Pokémon in any way you like. Shuffle the other cards and put them on
    the bottom of your deck."""
    top = ctx.deck_top(4)
    matches = [c for c in top if _is_basic_metal_energy(c)]
    picks = []
    if top:
        picks = await ctx.choose_cards(
            matches, max(len(matches), 1), minimum=0,
            prompt="Choose Basic Metal Energy cards to attach to your Pokémon.",
            display_cards=top,
        )
        candidates = ctx.my_pokemon_in_play()
        if picks and candidates:
            await distribute_energy(ctx, picks, candidates)
    others = [c for c in top if c not in picks]
    random.shuffle(others)
    for card in others:
        await ctx.put_on_bottom_of_deck(card)


card = PokemonCardDef(
    guid="e177c9aa-3ddc-50bb-822f-9ee2f3351474",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    display_name="Metang",
    searchable_by=["Metang", "Stage 1", "Metang"],
    subtypes=["Stage 1"],
    collector_number=114,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Beldum.Name",
    family_id=374,
    abilities=[
        Ability(
            title="Metal Maker",
            game_text="Once during your turn, you may look at the top 4 cards of your deck and attach any number of Basic [M] Energy cards you find there to your Pokémon in any way you like. Shuffle the other cards and put them on the bottom of your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=metal_maker,
        ),
        Attack(
            title="Beam",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
