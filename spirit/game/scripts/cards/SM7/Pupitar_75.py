from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ad787b36-64e8-59ca-b682-89d6277c29e5',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name',
    display_name='Pupitar',
    searchable_by=['Pupitar', 'Stage 1', 'Pupitar'],
    subtypes=['Stage 1'],
    collector_number=75,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name',
    family_id=246,
    abilities=[
        Attack(
            title='Skull Bash',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title='Dust Devil',
            game_text="This attack does 20 damage to each non-Fighting Pokémon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 2},
            effect=standard_attack,
        ),
    ],
)
