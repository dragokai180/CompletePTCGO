from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import search_to_hand
from spirit.game.models.board import BoardState
from spirit.game.session.effects import is_evolution_pokemon


def evolutionary_guidance_condition(board, player_id, pokemon):
    return bool(BoardState.attached_energies(pokemon))


card = PokemonCardDef(
    guid="a3201faa-085b-5692-98bb-77c2d2e88241",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    display_name="Dragonair",
    searchable_by=["Dragonair","Stage 1","Dragonair"],
    subtypes=["Stage 1"],
    collector_number=151,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    family_id=147,
    abilities=[
        Ability(
            title="Evolutionary Guidance",
            game_text="Once during your turn, if this Pokémon has any Energy attached, you may use this Ability. Search your deck for an Evolution Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=evolutionary_guidance_condition,
            effect=search_to_hand(
                is_evolution_pokemon, count=1, minimum=0,
                prompt="Choose an Evolution Pokémon to put into your hand.",
            ),
        ),
        Attack(
            title="Tail Snap",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=60,
        ),
    ],
)
