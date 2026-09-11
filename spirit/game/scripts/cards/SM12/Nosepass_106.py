from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5f5eca12-35e8-51f6-90be-54d5fa458321',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nosepass.Name',
    display_name='Nosepass',
    searchable_by=['Nosepass', 'Basic', 'Nosepass'],
    subtypes=['Basic'],
    collector_number=106,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=299,
    abilities=[
        Attack(
            title='Draw Toward',
            game_text="Switch 1 of your opponent's Benched Pokémon with their Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Zap Cannon',
            game_text="This Pokémon can't use Zap Cannon during your next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
