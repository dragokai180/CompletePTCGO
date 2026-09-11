from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ad79583a-5eba-58e7-a41c-c366da380852',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sylveon.Name',
    display_name='Sylveon',
    searchable_by=['Sylveon', 'Stage 1', 'Sylveon'],
    subtypes=['Stage 1'],
    collector_number=87,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=700,
    abilities=[
        Attack(
            title='Wink Wink',
            game_text='Your opponent reveals their hand. You may discard a Supporter card you find there and use the effect of that card as the effect of this attack.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Magical Shot',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
