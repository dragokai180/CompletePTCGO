from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='186c7133-bfd1-57f8-a04f-2253a8a73b05',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name',
    display_name='Ekans',
    searchable_by=['Ekans', 'Basic', 'Ekans'],
    subtypes=['Basic'],
    collector_number=23,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=23,
    abilities=[
        Attack(
            title='Acid Spray',
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
