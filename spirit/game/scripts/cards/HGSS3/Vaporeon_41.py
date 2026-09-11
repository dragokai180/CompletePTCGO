from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a78cffa0-a035-5d17-b0c2-f5696cfa6e43',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeon.Name',
    display_name='Vaporeon',
    searchable_by=['Vaporeon', 'Stage 1', 'Vaporeon'],
    subtypes=['Stage 1'],
    collector_number=41,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Attack(
            title='Spiral Drain',
            game_text='Remove 2 damage counters from Vaporeon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Dual Splash',
            game_text="Choose 2 of your opponent's Pokémon. This attack does 30 damage to each of them. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
