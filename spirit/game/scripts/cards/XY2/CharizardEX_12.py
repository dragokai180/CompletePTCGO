from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7b5dfc0b-cc2d-562d-bd71-5444ea2ebd49',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.CharizardEX.Name',
    display_name='Charizard-EX',
    searchable_by=['Charizard-EX', 'Basic', 'EX', 'CharizardEX'],
    subtypes=['Basic', 'EX'],
    collector_number=12,
    set_code='XY2',
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
            title='Wing Attack',
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
        Attack(
            title='Combustion Blast',
            game_text="This Pokémon can't use Combustion Blast during your next turn.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
