from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b59c8b79-1069-5a8c-85d2-e1ef64fe95d9',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Celebi.Name',
    display_name='Celebi',
    searchable_by=['Celebi', 'Basic', 'Celebi'],
    subtypes=['Basic'],
    collector_number=4,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=251,
    abilities=[
        Attack(
            title='Time Spiral',
            game_text="Devolve 1 of your opponent's evolved Pokémon by removing the highest Stage Evolution card from it. Your opponent shuffles that card into their deck.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Mind Bend',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
