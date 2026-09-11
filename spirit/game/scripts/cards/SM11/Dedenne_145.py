from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='71d2e333-3724-597a-8dd2-a0ccaf80aa23',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dedenne.Name',
    display_name='Dedenne',
    searchable_by=['Dedenne', 'Basic', 'Dedenne'],
    subtypes=['Basic'],
    collector_number=145,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=702,
    abilities=[
        Attack(
            title='Return',
            game_text='You may draw cards until you have 6 cards in your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
