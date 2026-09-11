from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='34811b17-015b-5004-9d44-6e81a4cbae0d',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mimikyu.Name',
    display_name='Mimikyu',
    searchable_by=['Mimikyu', 'Basic', 'Mimikyu'],
    subtypes=['Basic'],
    collector_number=97,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=778,
    abilities=[
        Ability(
            title='Shadow Box',
            game_text="Pokémon-GX that have any damage counters on them (both yours and your opponent's) have no Abilities.",
            passive=standard_passive("Pokémon-GX that have any damage counters on them (both yours and your opponent's) have no Abilities."),
        ),
        Attack(
            title='Tail Trickery',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
