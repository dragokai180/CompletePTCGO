from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='71a8385f-185a-50c2-a839-514416507464',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name',
    display_name='Eelektrik',
    searchable_by=['Eelektrik', 'Stage 1', 'Eelektrik'],
    subtypes=['Stage 1'],
    collector_number=45,
    set_code='SM3',
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
            title='Small Appetite',
            game_text="If your opponent's Active Pokémon's maximum HP is 100 or more, this attack does nothing.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
