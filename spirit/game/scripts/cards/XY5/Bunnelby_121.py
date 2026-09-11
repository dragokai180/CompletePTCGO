from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3c22761e-f127-577f-a8b1-553445779489',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bunnelby.Name',
    display_name='Bunnelby',
    searchable_by=['Bunnelby', 'Basic', 'Bunnelby'],
    subtypes=['Basic'],
    collector_number=121,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=659,
    abilities=[
        Attack(
            title='Burrow',
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Rototiller',
            game_text='Shuffle a card from your discard pile into your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
    passive=standard_passive("This Pokémon may attack twice a turn. (If the first attack Knocks Out your opponent's Active Pokémon, you may attack again after your opponent chooses a new Active Pokémon.)"),
)
