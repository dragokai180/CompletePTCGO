from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e1417564-6934-525e-9f7f-fda2e099096e',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lunatone.Name',
    display_name='Lunatone',
    searchable_by=['Lunatone', 'Basic', 'Lunatone'],
    subtypes=['Basic'],
    collector_number=61,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=337,
    abilities=[
        Ability(
            title='Sol Shade',
            game_text="If you have Solrock in play, Fire Pokémon in play (both yours and your opponent's) have no Abilities, except Pokémon-GX and Pokémon-EX.",
            passive=standard_passive("If you have Solrock in play, Fire Pokémon in play (both yours and your opponent's) have no Abilities, except Pokémon-GX and Pokémon-EX."),
        ),
        Attack(
            title='Psyshock',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
