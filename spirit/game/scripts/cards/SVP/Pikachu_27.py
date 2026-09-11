from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9060c5b6-9eb6-5925-9e67-a35fc820880f',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name',
    display_name='Pikachu',
    searchable_by=['Pikachu', 'Basic', 'Pikachu'],
    subtypes=['Basic'],
    collector_number=27,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=25,
    abilities=[
        Attack(
            title='Adventuring Together',
            game_text='This attack does 10 more damage for each of your Benched Pokémon.',
            cost={PokemonTypes.LIGHTNING: 3},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
