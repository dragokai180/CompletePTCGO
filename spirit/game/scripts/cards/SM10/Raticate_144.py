from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3c7ed2a5-815a-5ac1-8532-29fe8a26b1eb',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Raticate.Name',
    display_name='Raticate',
    searchable_by=['Raticate', 'Stage 1', 'Raticate'],
    subtypes=['Stage 1'],
    collector_number=144,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name',
    family_id=19,
    abilities=[
        Attack(
            title='Escaping Incisors',
            game_text="If your opponent's Active Pokémon is an Evolution Pokémon, switch this Pokémon with 1 of your Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
