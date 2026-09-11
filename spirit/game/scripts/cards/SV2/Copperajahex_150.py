from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6715b771-16e6-522f-b53b-b93cdcda23c2',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Copperajahex.Name',
    display_name='Copperajah ex',
    searchable_by=['Copperajah ex', 'Stage 1', 'ex', 'Copperajahex'],
    subtypes=['Stage 1', 'ex'],
    collector_number=150,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=300,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cufant.Name',
    family_id=878,
    abilities=[
        Ability(
            title='Bronze Body',
            game_text='This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).',
            passive=standard_passive('This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Nosequake',
            game_text="This attack also does 30 damage to each of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=260,
            effect=standard_attack,
        ),
    ],
)
