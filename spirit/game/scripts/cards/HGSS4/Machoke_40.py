from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bcb25d4a-d7d4-5143-9b5a-a767b86dd6ef',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Machoke.Name',
    display_name='Machoke',
    searchable_by=['Machoke', 'Stage 1', 'Machoke'],
    subtypes=['Stage 1'],
    collector_number=40,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name',
    family_id=66,
    abilities=[
        Attack(
            title='Knuckle Down',
            game_text="This attack's damage isn't affected by Poké-Powers, Poké-Bodies, or any other effects on the Defending Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Strength',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
