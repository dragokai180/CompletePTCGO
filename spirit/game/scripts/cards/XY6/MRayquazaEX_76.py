from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c3816cd6-3934-5e56-baf4-77f2f64f1c4d',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MRayquazaEX.Name',
    display_name='M Rayquaza-EX',
    searchable_by=['M Rayquaza-EX', 'MEGA', 'EX', 'MRayquazaEX'],
    subtypes=['MEGA', 'EX'],
    collector_number=76,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=220,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.RayquazaEX.Name',
    family_id=384,
    abilities=[
        Attack(
            title='Emerald Break',
            game_text='This attack does 30 damage times the number of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
    passive=standard_passive('You may play this card from your hand to evolve a Pokémon during your first turn or the turn you play that Pokémon.'),
)
