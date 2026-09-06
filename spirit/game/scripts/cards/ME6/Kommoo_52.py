from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card, deck_nonempty
from spirit.game.card_effects.support_common import look_top_attach_energy


def _can_look(board, player_id, pokemon=None):
    return deck_nonempty(board, player_id)


def _is_dragon_pokemon(pokemon):
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.DRAGON.value in types


card = PokemonCardDef(
    guid="1b0d63b0-940b-58ae-8075-dfc572f355a2",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Kommoo.Name",
    display_name="Kommo-o",
    searchable_by=["Kommo-o","Stage 2","Kommoo"],
    subtypes=["Stage 2"],
    collector_number=52,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Hakamoo.Name",
    family_id=782,
    abilities=[
        Ability(
            title="Scale Beat",
            game_text="You may use this Ability once during your turn. Look at the top 6 cards of your deck and attach any number of Basic Energy cards you find there to your [N] Pokémon in any way you like. Shuffle the other cards back into your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_can_look,
            effect=look_top_attach_energy(
                6, predicate=is_basic_energy_card, target_pred=_is_dragon_pokemon,
            ),
        ),
        Attack(
            title="Hammer In",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=170,
        ),
    ],
)
