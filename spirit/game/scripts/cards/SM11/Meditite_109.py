from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='68a7ffad-622e-5897-ab24-d8714a88a9e8',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Meditite.Name',
    display_name='Meditite',
    searchable_by=['Meditite', 'Basic', 'Meditite'],
    subtypes=['Basic'],
    collector_number=109,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=307,
    abilities=[
        Attack(
            title='Spirited Headbutt',
            game_text="This Pokémon can't use Spirited Headbutt during your next turn.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
