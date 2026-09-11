from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d7c7bcad-aca6-567b-b61d-adc827713d57',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanTauros.Name',
    display_name='Paldean Tauros',
    searchable_by=['Paldean Tauros', 'Basic', 'PaldeanTauros'],
    subtypes=['Basic'],
    collector_number=41,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=128,
    abilities=[
        Attack(
            title='Raging Horns',
            game_text='This attack does 10 more damage for each damage counter on this Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Aqua Dive',
            game_text="This attack does 60 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
