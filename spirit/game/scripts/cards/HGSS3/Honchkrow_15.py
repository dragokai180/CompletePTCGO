from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='de62af38-cb7c-5eca-b6d5-6724d9ed60f0',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Honchkrow.Name',
    display_name='Honchkrow',
    searchable_by=['Honchkrow', 'Stage 1', 'Honchkrow'],
    subtypes=['Stage 1'],
    collector_number=15,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name',
    family_id=198,
    abilities=[
        Attack(
            title='Whirlwind',
            game_text='Your opponent switches the Defending Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Blindside',
            game_text="Choose 1 of your opponent's Pokémon that has any damage counters on it. This attack does 50 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 2},
            effect=standard_attack,
        ),
    ],
)
