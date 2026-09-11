from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="35568388-a7fc-55c8-a32d-c7997a872d06",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsZekrom.Name",
    display_name="N's Zekrom",
    searchable_by=["N's Zekrom", "Basic", "NsZekrom"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="MEP",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    abilities=[
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=standard_attack,
        ),
        Attack(
            title="Rampaging Thunder",
            game_text="During your next turn, this Pokémon can't use attacks.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=250,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
