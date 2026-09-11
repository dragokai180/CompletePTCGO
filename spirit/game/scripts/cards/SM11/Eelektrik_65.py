from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a838f627-ec1f-5953-8041-870b7d7fbf7f',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name',
    display_name='Eelektrik',
    searchable_by=['Eelektrik', 'Stage 1', 'Eelektrik'],
    subtypes=['Stage 1'],
    collector_number=65,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name',
    family_id=602,
    abilities=[
        Attack(
            title='Overspark',
            game_text='Discard all Lightning Energy from this Pokémon. This attack does 30 damage for each card you discarded in this way.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
