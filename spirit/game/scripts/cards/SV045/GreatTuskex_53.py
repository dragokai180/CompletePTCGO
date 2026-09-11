from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b515715a-f03d-59c9-ab70-9a4e7ae20569',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GreatTuskex.Name',
    display_name='Great Tusk ex',
    searchable_by=['Great Tusk ex', 'Basic', 'ex', 'Ancient', 'GreatTuskex'],
    subtypes=['Basic', 'ex', 'Ancient'],
    collector_number=53,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=250,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=984,
    abilities=[
        Ability(
            title='Quaking Demolition',
            game_text='Once at the end of your turn (after your attack), if this Pokémon is in the Active Spot, you must discard the top 5 cards of your deck.',
            effect=standard_ability,
            trigger=Triggers.END_OF_TURN,
        ),
        Attack(
            title='Great Bash',
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=260,
            effect=standard_attack,
        ),
    ],
)
