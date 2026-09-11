from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4bc1f9fc-6b1d-5623-8869-3f83c8b4319e',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ledian.Name',
    display_name='Ledian',
    searchable_by=['Ledian', 'Stage 1', 'Ledian'],
    subtypes=['Stage 1'],
    collector_number=25,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Ledyba.Name',
    family_id=165,
    abilities=[
        Attack(
            title='Quick Draw',
            game_text='Draw 3 cards.',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Swift',
            game_text="This attack's damage isn't affected by Weakness, Resistance, Poké-Powers, Poké-Bodies, or any other effects on the Defending Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
