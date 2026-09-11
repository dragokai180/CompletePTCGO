from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d8a37b55-3735-524a-a8d7-978c2d660fd8',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeot.Name',
    display_name='Pidgeot',
    searchable_by=['Pidgeot', 'Stage 2', 'Pidgeot'],
    subtypes=['Stage 2'],
    collector_number=29,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name',
    family_id=16,
    abilities=[
        Attack(
            title='Headwind',
            game_text="During your opponent's next turn, the attack cost of each of the Defending Pokémon's attacks is ColorlessColorless more.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Quick Attack',
            game_text='Flip a coin. If heads, this attack does 40 damage plus 30 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
