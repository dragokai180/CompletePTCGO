from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4605e27b-d85b-53f5-8684-b4f57ee0ac7e',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Garchomp.Name',
    display_name='Garchomp',
    searchable_by=['Garchomp', 'Stage 2', 'Garchomp'],
    subtypes=['Stage 2'],
    collector_number=99,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FAIRY,
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
