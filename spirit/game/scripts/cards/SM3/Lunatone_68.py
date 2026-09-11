from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='77d25720-a1b6-5d76-b35c-6d5af1bf7c5a',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lunatone.Name',
    display_name='Lunatone',
    searchable_by=['Lunatone', 'Basic', 'Lunatone'],
    subtypes=['Basic'],
    collector_number=68,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=337,
    abilities=[
        Ability(
            title='Heal Block',
            game_text="If you have Solrock in play, Pokémon (both yours and your opponent's) can't be healed.",
            passive=standard_passive("If you have Solrock in play, Pokémon (both yours and your opponent's) can't be healed."),
        ),
        Attack(
            title='Lunar Blast',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
