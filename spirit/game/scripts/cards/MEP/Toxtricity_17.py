from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)
from spirit.game.scripts.cards.ME2.Toxtricity_68 import (
    sinister_surge, _sinister_surge_condition,
)


card = PokemonCardDef(
    guid="0930fc50-e112-52da-8140-fad197eada98",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricity.Name",
    display_name="Toxtricity",
    searchable_by=["Toxtricity", "Stage 1", "Toxtricity"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="MEP",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    abilities=[
        Ability(
            title="Sinister Surge",
            game_text="Once during your turn, you may use this Ability. Search your deck for a Basic [ [Darkness] ] Energy card and attach it to 1 of your Benched [ [Darkness] ] Pokémon. Then, shuffle your deck. If you attached Energy to a Pokémon in this way, place 2 damage counters on that Pokémon.",
            effect=sinister_surge,
            condition=_sinister_surge_condition,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
