from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack
from spirit.game.card_effects.passives_common import is_in_active_spot
from spirit.game.session.passives import Passive, carrier_pokemon


class BoostedEvolutionPassive(Passive):
    """While Active, this Pokémon can evolve on turn 1 / the turn it was played."""

    def may_evolve_early(self, pokemon, carrier):
        return carrier_pokemon(carrier) is pokemon and is_in_active_spot(pokemon)


card = PokemonCardDef(
    guid="16a8a44a-7ebf-5d76-bead-70a1ab1a18c3",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    display_name="Eevee",
    searchable_by=["Eevee", "Basic", "Eevee"],
    subtypes=["Basic"],
    collector_number=143,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=133,
    abilities=[
        Ability(
            title="Boosted Evolution",
            game_text=(
                "As long as this Pokémon is in the Active Spot, it can evolve "
                "during your first turn or the turn you play it."
            ),
            passive=BoostedEvolutionPassive(),
        ),
        Attack(
            title="Reckless Charge",
            game_text="This Pokémon also does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=recoil_attack(10),
        ),
    ],
)
