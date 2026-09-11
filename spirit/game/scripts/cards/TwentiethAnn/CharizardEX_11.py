from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d3739a5b-de0a-565f-8c91-714d293da945',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.CharizardEX.Name',
    display_name='Charizard-EX',
    searchable_by=['Charizard-EX', 'Basic', 'EX', 'CharizardEX'],
    subtypes=['Basic', 'EX'],
    collector_number=11,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=6,
    abilities=[
        Attack(
            title='Flame Cloak',
            game_text='Attach a Fire Energy card from your discard pile to this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Burning Breath',
            game_text='Flip 2 coins. This attack does 40 more damage for each heads.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
