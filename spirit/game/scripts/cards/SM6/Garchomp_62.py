from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d6f11d1c-7122-54d3-a13b-d07b12ecd3d3',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Garchomp.Name',
    display_name='Garchomp',
    searchable_by=['Garchomp', 'Stage 2', 'Garchomp'],
    subtypes=['Stage 2'],
    collector_number=62,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name',
    family_id=443,
    abilities=[
        Attack(
            title='Quick Dive',
            game_text="This attack does 50 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Royal Blades',
            game_text='If you played Cynthia from your hand during this turn, this attack does 100 more damage.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
