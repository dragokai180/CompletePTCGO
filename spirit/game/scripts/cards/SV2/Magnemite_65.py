from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dce70512-6409-5ce3-93ee-8512fce2aac7',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name',
    display_name='Magnemite',
    searchable_by=['Magnemite', 'Basic', 'Magnemite'],
    subtypes=['Basic'],
    collector_number=65,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=81,
    abilities=[
        Attack(
            title='Magnetic Charge',
            game_text='Attach up to 2 Basic Lightning Energy cards from your discard pile to 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Speed Ball',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
