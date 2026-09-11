from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='acb9062b-b293-5326-9b7e-315dc922b365',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanTauros.Name',
    display_name='Paldean Tauros',
    searchable_by=['Paldean Tauros', 'Basic', 'PaldeanTauros'],
    subtypes=['Basic'],
    collector_number=108,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
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
            title='Combat Tackle',
            game_text='This Pokémon also does 30 damage to itself.',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
