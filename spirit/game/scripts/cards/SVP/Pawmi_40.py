from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='652aa2b2-f2c7-5e0a-8145-84ae9b4ffdd9',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pawmi.Name',
    display_name='Pawmi',
    searchable_by=['Pawmi', 'Basic', 'Pawmi'],
    subtypes=['Basic'],
    collector_number=40,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=921,
    abilities=[
        Attack(
            title='Static Slap',
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
