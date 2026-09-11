from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4d1e5979-e6b1-5285-a0a3-c5b5f993b29d',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lickilicky.Name',
    display_name='Lickilicky',
    searchable_by=['Lickilicky', 'Stage 1', 'Lickilicky'],
    subtypes=['Stage 1'],
    collector_number=38,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lickitung.Name',
    family_id=108,
    abilities=[
        Attack(
            title='Licking Shot',
            game_text="Choose 1 of your opponent's Pokémon. This attack does 10 damage to that Pokémon for each Energy attached to Lickilicky. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Stick and Absorb',
            game_text="Remove 2 damage counters from Lickilicky. The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
