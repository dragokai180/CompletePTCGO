from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4bf10b93-80e9-5547-a32e-c612f681a46a',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GardevoirEX.Name',
    display_name='Gardevoir-EX',
    searchable_by=['Gardevoir-EX', 'Basic', 'EX', 'GardevoirEX'],
    subtypes=['Basic', 'EX'],
    collector_number=78,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=282,
    abilities=[
        Attack(
            title='Link Blast',
            game_text="If this Pokémon and your opponent's Active Pokémon have the same amount of Energy attached to them, this attack does 70 more damage.",
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Luminous Blade',
            game_text='Discard an Energy attached to this Pokémon.',
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
