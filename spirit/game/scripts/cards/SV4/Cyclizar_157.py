from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a606fc74-c089-50b2-aeae-037fc8be662c',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cyclizar.Name',
    display_name='Cyclizar',
    searchable_by=['Cyclizar', 'Basic', 'Cyclizar'],
    subtypes=['Basic'],
    collector_number=157,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=967,
    abilities=[
        Attack(
            title='Ram',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Driving Buddy',
            game_text='If you played a Supporter card from your hand during this turn, this attack does 70 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
