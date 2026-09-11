from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f6341a32-dc75-5264-b359-b32e8954db83',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name',
    display_name='Torchic',
    searchable_by=['Torchic', 'Basic', 'Torchic'],
    subtypes=['Basic'],
    collector_number=26,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=255,
    abilities=[
        Attack(
            title='Flare Bonus',
            game_text='Discard a Fire Energy card from your hand. If you do, draw 2 cards.',
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Claw',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
    passive=standard_passive("This Pokémon may attack twice a turn. (If the first attack Knocks Out your opponent's Active Pokémon, you may attack again after your opponent chooses a new Active Pokémon.)"),
)
