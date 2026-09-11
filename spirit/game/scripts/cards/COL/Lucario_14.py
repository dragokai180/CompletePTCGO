from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3f2eac00-d490-5a16-bcad-36b36818abb6',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name',
    display_name='Lucario',
    searchable_by=['Lucario', 'Stage 1', 'Lucario'],
    subtypes=['Stage 1'],
    collector_number=14,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name',
    family_id=447,
    abilities=[
        Attack(
            title='Dimension Sphere',
            game_text='Does 30 damage plus 20 more damage for each of your Pokémon in the Lost Zone.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Sky Uppercut',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
