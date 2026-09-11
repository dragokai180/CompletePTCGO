from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0d305f42-0586-5726-9579-04f7a0c7e21b',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name',
    display_name='Snorunt',
    searchable_by=['Snorunt', 'Basic', 'Snorunt'],
    subtypes=['Basic'],
    collector_number=37,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=361,
    abilities=[
        Attack(
            title='Ice Shard',
            game_text="If your opponent's Active Pokémon is a Fighting Pokémon, this attack does 30 more damage.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
