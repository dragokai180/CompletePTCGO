from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a533657e-2f90-5a8f-8ba6-6199f518f53c',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Xerneas.Name',
    display_name='Xerneas',
    searchable_by=['Xerneas', 'Basic', 'Xerneas'],
    subtypes=['Basic'],
    collector_number=73,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=716,
    abilities=[
        Attack(
            title='Lead',
            game_text='Search your deck for a Supporter card, reveal it, and put it into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bright Horns',
            game_text="This Pokémon can't use Bright Horns during your next turn.",
            cost={PokemonTypes.FAIRY: 3},
            damage=130,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
