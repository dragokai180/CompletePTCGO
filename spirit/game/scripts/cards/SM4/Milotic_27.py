from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9994afde-cdf6-578a-960c-72acaefd928e',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Milotic.Name',
    display_name='Milotic',
    searchable_by=['Milotic', 'Stage 1', 'Milotic'],
    subtypes=['Stage 1'],
    collector_number=27,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Feebas.Name',
    family_id=349,
    abilities=[
        Attack(
            title='TLC',
            game_text="Shuffle 1 of your opponent's Benched Pokémon that has any damage counters on it and all cards attached to it into their deck.",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Ocean Cyclone',
            game_text="This attack does 10 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
