from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e1b5dc1b-2d56-50d5-b4dd-9cc58215ee54',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kabuto.Name',
    display_name='Kabuto',
    searchable_by=['Kabuto', 'Stage 1', 'Kabuto'],
    subtypes=['Stage 1'],
    collector_number=140,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AntiqueDomeFossil.Name',
    family_id=140,
    abilities=[
        Attack(
            title='Double Scratch',
            game_text='Flip 2 coins. This attack does 70 damage for each heads.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
