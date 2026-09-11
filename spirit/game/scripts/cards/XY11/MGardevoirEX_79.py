from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f4a11675-a714-5089-a2fc-63a36f471813',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MGardevoirEX.Name',
    display_name='M Gardevoir-EX',
    searchable_by=['M Gardevoir-EX', 'MEGA', 'EX', 'MGardevoirEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=79,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=210,
    elements=[PokemonTypes.FAIRY, PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirEX.Name',
    family_id=282,
    abilities=[
        Attack(
            title='Despair Ray',
            game_text='Discard as many of your Benched Pokémon as you like. This attack does 10 more damage for each Benched Pokémon you discarded in this way.',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
